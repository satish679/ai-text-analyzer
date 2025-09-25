document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const text = document.getElementById("textInput").value;
 
  // Sentiment
  const resSent = await fetch("http://127.0.0.1:8000/sentiment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });
  const dataSent = await resSent.json();
  document.getElementById("sentiment").innerText = dataSent.sentiment;
 
  // Summary
  const resSum = await fetch("http://127.0.0.1:8000/summarize", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });
  const dataSum = await resSum.json();
  document.getElementById("summary").innerText = dataSum.summary;
});
 