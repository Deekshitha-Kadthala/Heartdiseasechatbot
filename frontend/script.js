const API_BASE_URL = "http://127.0.0.1:8000";

// Upload Image and Get Prediction
async function uploadImage() {

    const imageInput = document.getElementById("imageInput");

    if (!imageInput.files.length) {
        alert("Please select an image first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", imageInput.files[0]);

    document.getElementById("predictionResult").innerHTML =
        "Analyzing image...";

    try {

        const response = await fetch(
            `${API_BASE_URL}/predict`,
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        document.getElementById("predictionResult").innerHTML = `
            <h3>${data.prediction}</h3>
            <p>Confidence: ${data.confidence}%</p>
            <p>${data.message}</p>
        `;

    } catch (error) {

        document.getElementById("predictionResult").innerHTML =
            "Error connecting to server.";

        console.error(error);
    }
}

// Send Chat Message
async function sendMessage() {

    const input = document.getElementById("userMessage");
    const chatBox = document.getElementById("chatBox");

    const message = input.value.trim();

    if (!message) return;

    chatBox.innerHTML += `
        <div class="user-message">
            You: ${message}
        </div>
    `;

    input.value = "";

    try {

        const response = await fetch(
            `${API_BASE_URL}/chat`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: message
                })
            }
        );

        const data = await response.json();

        chatBox.innerHTML += `
            <div class="bot-message">
                Bot: ${data.answer}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {

        chatBox.innerHTML += `
            <div class="bot-message">
                Bot: Server connection failed.
            </div>
        `;

        console.error(error);
    }
}