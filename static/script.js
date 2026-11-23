
// =====================================
// DOM ELEMENTS
// =====================================

const input = document.getElementById("messageInput");
const button = document.getElementById("sendButton");
const chat = document.getElementById("chat");
const recentChats = document.getElementById("recentChats");
const newChatButton = document.getElementById("newChatButton");


// =====================================
// STATE
// =====================================

let messages = [];
let currentChatId = null;
let isSending = false;


// =====================================
// WELCOME SCREEN
// =====================================

function showWelcomeScreen() {

    chat.innerHTML = `
        <div class="welcome">
            <div class="welcome-icon">I</div>

            <h1>How can I help you?</h1>

            <p>
                Ask me anything. I'll explain it clearly
                and help you understand it step by step.
            </p>
        </div>
    `;

}


// =====================================
// NEW CHAT
// =====================================

function startNewChat() {

    if (isSending) return;

    messages = [];
    currentChatId = null;

    input.value = "";

    showWelcomeScreen();

    loadChatHistory();

}


// =====================================
// ADD MESSAGE
// =====================================

function addMessage(text, sender) {

    const message = document.createElement("div");
    message.className = "message";

    // Avatar
    const avatar = document.createElement("div");

    avatar.className =
        sender === "user"
            ? "avatar user-avatar"
            : "avatar ai-avatar";

    avatar.textContent = sender === "user" ? "U" : "I";

    // Content
    const content = document.createElement("div");
    content.className = "message-content";

    // Name
    const name = document.createElement("div");
    name.className = "message-name";

    name.textContent =
        sender === "user" ? "You" : "Infinix";

    // Message body
    const messageText = document.createElement("div");

    messageText.className =
        sender === "user" ? "user-text" : "ai-text";

    if (sender === "ai") {

        // Render Markdown safely
        const parsedHTML = marked.parse(text);

        messageText.innerHTML = DOMPurify.sanitize(parsedHTML);

        // Syntax highlighting
        messageText.querySelectorAll("pre code").forEach(block => {
            Prism.highlightElement(block);
        });

    } else {

        messageText.textContent = text;

    }

    // Assemble
    content.appendChild(name);
    content.appendChild(messageText);

    message.appendChild(avatar);
    message.appendChild(content);

    chat.appendChild(message);

    // Scroll down
    chat.scrollTop = chat.scrollHeight;

}


// =====================================
// SEND MESSAGE
// =====================================

async function sendMessage() {

    const text = input.value.trim();

    if (!text || isSending) return;

    // Remove welcome screen
    const welcome = document.querySelector(".welcome");

    if (welcome) {
        welcome.remove();
    }

    // Show user message
    addMessage(text, "user");

    // Add to conversation
    messages.push({
        role: "user",
        content: text
    });

    // Clear input
    input.value = "";

    // Disable sending
    isSending = true;
    button.disabled = true;
    input.disabled = true;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                messages: messages,
                chat_id: currentChatId
            })

        });

        const data = await response.json();

        if (!response.ok) {

            throw new Error(
                data.error || `Server error: ${response.status}`
            );

        }

        if (!data.response || data.chat_id == null) {

            throw new Error("Invalid response from server");

        }

        console.log("AI RESPONSE:", data.response);

        // Update conversation ID
        currentChatId = data.chat_id;

        // Save AI response
        messages.push({
            role: "assistant",
            content: data.response
        });

        // Display AI response
        addMessage(data.response, "ai");

        // Refresh sidebar
        await loadChatHistory();

    }

    catch (error) {

        console.error("CHAT ERROR:", error);

        // Remove failed user message from local state
        messages.pop();

        // Restore text for retry
        input.value = text;

        addMessage(
            `Sorry, something went wrong: ${error.message}`,
            "ai"
        );

    }

    finally {

        isSending = false;

        button.disabled = false;
        input.disabled = false;

        input.focus();

    }

}


// =====================================
// LOAD CHAT HISTORY
// =====================================

async function loadChatHistory() {

    try {

        const response = await fetch("/chats");

        if (!response.ok) {
            throw new Error("Failed to fetch chat history");
        }

        const data = await response.json();

        console.log("CHAT HISTORY:", data.chats);

        recentChats.innerHTML = "";

        if (!Array.isArray(data.chats) || data.chats.length === 0) {

            recentChats.textContent = "No conversations yet";

            return;
        }

        data.chats.forEach(chatItem => {

            const historyItem = document.createElement("div");

            historyItem.className = "history-item";

            // Active state
            if (String(chatItem.id) === String(currentChatId)) {
                historyItem.classList.add("active");
            }

            // Title
            const title = document.createElement("span");

            title.className = "history-title";

            title.textContent = chatItem.user_message;

            // Delete button
            const deleteButton = document.createElement("button");

            deleteButton.textContent = "×";
            deleteButton.className = "delete-chat";

            deleteButton.addEventListener("click", async event => {

                event.stopPropagation();

                await deleteConversation(chatItem.id);

            });

            // Assemble
            historyItem.appendChild(title);
            historyItem.appendChild(deleteButton);

            // Open conversation
            historyItem.addEventListener("click", () => {

                loadConversation(chatItem.id);

            });

            recentChats.appendChild(historyItem);

        });

    }

    catch (error) {

        console.error("HISTORY ERROR:", error);

        recentChats.textContent = "Unable to load conversations";

    }

}


// =====================================
// LOAD CONVERSATION
// =====================================

async function loadConversation(chatId) {

    if (isSending) return;

    try {

        const response = await fetch(`/chat/${chatId}`);

        if (!response.ok) {
            throw new Error("Failed to load conversation");
        }

        const data = await response.json();

        // Clear chat
        chat.innerHTML = "";

        // Restore messages
        messages = [
            {
                role: "user",
                content: data.user_message
            },
            {
                role: "assistant",
                content: data.ai_response
            }
        ];

        // Display messages
        addMessage(data.user_message, "user");
        addMessage(data.ai_response, "ai");

        // Update current ID
        currentChatId = data.id;

        // Refresh sidebar
        await loadChatHistory();

    }

    catch (error) {

        console.error("LOAD CHAT ERROR:", error);

    }

}


// =====================================
// DELETE CONVERSATION
// =====================================

async function deleteConversation(chatId) {

    if (isSending) return;

    try {

        const response = await fetch(
            `/chat/${chatId}`,
            {
                method: "DELETE"
            }
        );

        const data = await response.json();

        if (!response.ok || !data.success) {

            throw new Error(
                data.error || "Failed to delete conversation"
            );

        }

        // If deleting current conversation
        if (String(currentChatId) === String(chatId)) {

            messages = [];
            currentChatId = null;

            showWelcomeScreen();

        }

        // Refresh history
        await loadChatHistory();

    }

    catch (error) {

        console.error("DELETE ERROR:", error);

    }

}


// =====================================
// EVENT LISTENERS
// =====================================

// Send button
button.addEventListener("click", sendMessage);


// Enter sends, Shift + Enter creates new line
input.addEventListener("keydown", event => {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        sendMessage();

    }

});


// New chat
newChatButton.addEventListener("click", startNewChat);


// =====================================
// INITIALIZATION
// =====================================

loadChatHistory();
