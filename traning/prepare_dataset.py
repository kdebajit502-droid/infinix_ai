
import json
from pathlib import Path

DATASET = Path(__file__).parent / "dataset.jsonl"
OUTPUT = Path(__file__).parent / "validated_dataset.jsonl"


def main():
    if not DATASET.exists():
        raise FileNotFoundError(f"Missing dataset: {DATASET}")

    valid_examples = []

    with DATASET.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue

            try:
                example = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON on line {line_number}: {error}"
                ) from error

            messages = example.get("messages")

            if not isinstance(messages, list) or len(messages) < 2:
                raise ValueError(
                    f"Line {line_number}: invalid messages list"
                )

            if (
                messages[0].get("role") != "user"
                or messages[-1].get("role") != "assistant"
            ):
                raise ValueError(
                    f"Line {line_number}: expected user first, assistant last"
                )

            if any(
                not isinstance(m, dict)
                or m.get("role") not in {"user", "assistant", "system"}
                or not isinstance(m.get("content"), str)
                or not m["content"].strip()
                for m in messages
            ):
                raise ValueError(
                    f"Line {line_number}: invalid message"
                )

            valid_examples.append({"messages": messages})

    with OUTPUT.open("w", encoding="utf-8") as file:
        for example in valid_examples:
            file.write(json.dumps(example, ensure_ascii=False) + "\n")

    print(f"Validated {len(valid_examples)} examples.")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
