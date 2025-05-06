document.addEventListener("DOMContentLoaded", () => {
    const chatAvatar = document.getElementById("chat-avatar");
    const chatMessages = document.getElementById("chat-messages");
    const chatInputContainer = document.getElementById("chat-input-container");
    const chatInput = document.getElementById("chat-input");
    const sendBtn = document.getElementById("send-btn");

    // Show initial message after 5 seconds
    setTimeout(() => {
        chatMessages.classList.remove("hidden");
        chatInputContainer.classList.remove("hidden");
    }, 5000);

    // Toggle chat manually on avatar click
    chatAvatar.addEventListener("click", () => {
        chatMessages.classList.toggle("hidden");
        chatInputContainer.classList.toggle("hidden");
    });

    // Send message to backend
    sendBtn.addEventListener("click", () => {
        const userMessage = chatInput.value.trim();
        if (!userMessage) return;

        appendMessage("user-message", userMessage);
        chatInput.value = "";

        fetch("/chatbot/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({ message: userMessage }),
        })
        .then(res => res.json())
        .then(data => {
            appendMessage("bot-message", data.reply);
        });
    });

    function appendMessage(className, message) {
        const msg = document.createElement("div");
        msg.className = className;
        msg.textContent = message;
        chatMessages.appendChild(msg);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
