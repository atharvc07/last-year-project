// dashboard/dashboard.js

// Backend API URL mapping
const BACKEND_URL = "http://127.0.0.1:5000/predict";

document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("predictionForm");
    const resultBox = document.getElementById("resultBox");
    const predictionResult = document.getElementById("predictionResult");
    const errorBox = document.getElementById("errorBox");

    // Buttons and Spinners
    const predictBtn = document.getElementById("predictBtn");
    const btnSpinner = document.getElementById("btnSpinner");

    form.addEventListener("submit", async (e) => {
        // Prevent page from reloading
        e.preventDefault();

        // Reset the UI before prediction
        errorBox.classList.add("d-none");
        resultBox.classList.add("d-none");

        // Show spinner
        btnSpinner.classList.remove("d-none");
        predictBtn.disabled = true;

        // Capture data from inputs
        const formData = {
            "Weather Conditions": document.getElementById("Weather Conditions").value,
            "Road Type": document.getElementById("Road Type").value,
            "Road Condition": document.getElementById("Road Condition").value,
            "Lighting Conditions": document.getElementById("Lighting Conditions").value,
            "Driver Age": parseInt(document.getElementById("Driver Age").value, 10),
            "Speed Limit (km/h)": parseInt(document.getElementById("Speed Limit (km/h)").value, 10),
            "Alcohol Involvement": document.getElementById("Alcohol Involvement").value
        };

        try {
            // Send the POST request to Flask
            console.log("Sending Prediction Request:", formData);

            const response = await fetch(BACKEND_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

            // Parse response
            const responseData = await response.json();

            if (!response.ok) {
                throw new Error("Server Error: " + (responseData.error || "Unknown Error"));
            }

            const severity = responseData.predicted_severity;

            // Extract UI elements
            predictionResult.innerText = severity;

            // Apply Dynamic color logic based on Severity text
            resultBox.className = "p-3 rounded text-center"; // reset classes

            if (severity.toLowerCase().includes("fatal")) {
                resultBox.classList.add("bg-danger-subtle");
            } else if (severity.toLowerCase().includes("serious")) {
                resultBox.classList.add("bg-warning-subtle");
            } else {
                resultBox.classList.add("bg-success-subtle");
            }

            // Show result
            resultBox.classList.remove("d-none");

        } catch (error) {
            console.error("Prediction Error:", error);
            errorBox.classList.remove("d-none");
            errorBox.innerText = `Prediction Failed: ${error.message} \n(Make sure the Flask API is running at 127.0.0.1:5000)`;
        } finally {
            // Stop spinner
            btnSpinner.classList.add("d-none");
            predictBtn.disabled = false;
        }
    });
});
