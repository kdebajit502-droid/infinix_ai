
from flask import Flask, render_template, request, jsonify

from database import (
    init_db,
    get_chat_history,
    get_chat,
    delete_chat,
    save_chat,
    update_chat
)

from ai import chat_with_ai


# =========================================================
# FLASK CONFIGURATION
# =========================================================

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


# Initialize database
init_db()


# =========================================================
# FRONTEND
# =========================================================

@app.route("/")
def home():

    return render_template("index.html")


# =========================================================
# CHAT
# =========================================================

@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json(silent=True)

        if not isinstance(data, dict):

            return jsonify({
                "error": "Invalid JSON request"
            }), 400

        messages = data.get("messages", [])
        chat_id = data.get("chat_id")

        if not isinstance(messages, list) or not messages:

            return jsonify({
                "error": "Messages are required"
            }), 400

        # Validate messages
        if not all(
            isinstance(message, dict)
            and isinstance(message.get("content"), str)
            and isinstance(message.get("role"), str)
            for message in messages
        ):

            return jsonify({
                "error": "Invalid message format"
            }), 400

        # Find latest user message
        user_message = next(
            (
                message["content"]
                for message in reversed(messages)
                if message.get("role") == "user"
            ),
            None
        )

        if not user_message or not user_message.strip():

            return jsonify({
                "error": "User message not found"
            }), 400

        print("CHAT ROUTE CALLED")
        print("CHAT ID:", chat_id)

        # Generate AI response
        answer = chat_with_ai(messages)

        if not isinstance(answer, str) or not answer.strip():

            return jsonify({
                "error": "AI returned an empty response"
            }), 500

        # Save or update conversation
        if chat_id is None:

            chat_id = save_chat(
                user_message,
                answer
            )

        else:

            if (
                isinstance(chat_id, bool)
                or not isinstance(chat_id, int)
                or chat_id < 1
            ):

                return jsonify({
                    "error": "Invalid chat ID"
                }), 400

            updated = update_chat(
                chat_id,
                user_message,
                answer
            )

            if not updated:

                return jsonify({
                    "error": "Chat not found"
                }), 404

        print("AI ANSWER:", answer)

        return jsonify({
            "response": answer,
            "chat_id": chat_id
        })

    except Exception as error:

        print("CHAT ERROR:", error)

        return jsonify({
            "error": "Something went wrong while processing your message"
        }), 500


# =========================================================
# GET CHAT HISTORY
# =========================================================

@app.route("/chats", methods=["GET"])
def chats():

    try:

        history = get_chat_history(20)

        return jsonify({

            "chats": [

                {
                    "id": row[0],
                    "user_message": row[1],
                    "ai_response": row[2],
                    "created_at": row[3]
                }

                for row in history

            ]

        })

    except Exception as error:

        print("HISTORY ERROR:", error)

        return jsonify({
            "error": "Failed to load chat history"
        }), 500


# =========================================================
# GET SINGLE CHAT
# =========================================================

@app.route("/chat/<int:chat_id>", methods=["GET"])
def get_single_chat(chat_id):

    try:

        chat_data = get_chat(chat_id)

        if not chat_data:

            return jsonify({
                "error": "Chat not found"
            }), 404

        return jsonify({

            "id": chat_data[0],
            "user_message": chat_data[1],
            "ai_response": chat_data[2],
            "created_at": chat_data[3]

        })

    except Exception as error:

        print("GET CHAT ERROR:", error)

        return jsonify({
            "error": "Failed to retrieve conversation"
        }), 500


# =========================================================
# DELETE CHAT
# =========================================================

@app.route("/chat/<int:chat_id>", methods=["DELETE"])
def delete_single_chat(chat_id):

    try:

        deleted = delete_chat(chat_id)

        if not deleted:

            return jsonify({
                "success": False,
                "error": "Chat not found"
            }), 404

        return jsonify({
            "success": True
        })

    except Exception as error:

        print("DELETE ERROR:", error)

        return jsonify({
            "success": False,
            "error": "Failed to delete conversation"
        }), 500


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=False,
        use_reloader=False,
        threaded=False
    )
