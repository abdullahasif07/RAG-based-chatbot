function askQuestion() {
    let question = document.getElementById("question").value;
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.answer;
    });
}
