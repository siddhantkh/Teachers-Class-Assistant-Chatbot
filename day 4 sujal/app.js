function generateContent() {
  const topic = document.getElementById("topicInput").value.trim();
  const outputDiv = document.getElementById("output");

  if (!topic) {
    outputDiv.innerHTML = "<p style='color:red;'>⚠️ Please enter a topic.</p>";
    return;
  }

  // Mock generated content (in real MVP, this comes from API)
  const ideas = [
    `Interactive activity: Debate the importance of ${topic}`,
    `Group project: Create a poster explaining ${topic}`,
    `Experiment or demo related to ${topic}`
  ];

  const questions = [
    `What is the key concept behind ${topic}?`,
    `How does ${topic} impact our daily lives?`,
    `Explain ${topic} in simple terms.`,
    `Give a real-world example of ${topic}.`,
    `Why is ${topic} important to study?`
  ];

  outputDiv.innerHTML = `
    <h3>💡 Class Ideas:</h3>
    <ul>${ideas.map(i => `<li>${i}</li>`).join("")}</ul>
    <h3>❓ Practice Questions:</h3>
    <ul>${questions.map(q => `<li>${q}</li>`).join("")}</ul>
  `;
}
