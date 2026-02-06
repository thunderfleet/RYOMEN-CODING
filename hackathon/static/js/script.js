document.addEventListener("DOMContentLoaded", () => {
  // Navigation Handling
  const navBtns = document.querySelectorAll(".nav-btn");
  const sections = document.querySelectorAll(".tool-section");

  navBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      // Remove active class from all
      navBtns.forEach((b) => b.classList.remove("active"));
      sections.forEach((s) => s.classList.remove("active"));

      // Add active class to clicked
      btn.classList.add("active");
      const targetId = btn.getAttribute("data-target");
      document.getElementById(targetId).classList.add("active");
    });
  });

  // API Helper Function
  async function fetchAI(endpoint, data, btnElement, resultElementId) {
    const btnText = btnElement.querySelector(".btn-text");
    const loader = btnElement.querySelector(".loader");
    const resultContainer = document.getElementById(resultElementId);

    // UI Loading State
    btnElement.classList.add("loading");
    btnElement.disabled = true;

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const jsonResponse = await response.json();

      // Clear empty state
      resultContainer.classList.remove("empty");

      if (response.ok) {
        return jsonResponse.result; // Success
      } else {
        throw new Error(jsonResponse.error || "Something went wrong");
      }
    } catch (error) {
      resultContainer.innerHTML = `<div style="color: #ef4444; padding: 1rem; border: 1px solid #ef4444; border-radius: 0.5rem;">Error: ${error.message}</div>`;
      return null;
    } finally {
      // Restore UI
      btnElement.classList.remove("loading");
      btnElement.disabled = false;
    }
  }

  // Campaign Generator Form
  document
    .getElementById("campaign-form")
    .addEventListener("submit", async (e) => {
      e.preventDefault();
      const data = {
        product: document.getElementById("camp-product").value,
        audience: document.getElementById("camp-audience").value,
        platform: document.getElementById("camp-platform").value,
      };

      const result = await fetchAI(
        "/api/campaign",
        data,
        e.submitter,
        "camp-result",
      );
      if (result) {
        document.getElementById("camp-result").innerHTML =
          `<div class="result-content">${formatText(result)}</div>`;
      }
    });

  // Sales Pitch Generator Form
  document
    .getElementById("pitch-form")
    .addEventListener("submit", async (e) => {
      e.preventDefault();
      const data = {
        product: document.getElementById("pitch-product").value,
        persona: document.getElementById("pitch-persona").value,
      };

      const result = await fetchAI(
        "/api/pitch",
        data,
        e.submitter,
        "pitch-result",
      );
      if (result) {
        document.getElementById("pitch-result").innerHTML =
          `<div class="result-content">${formatText(result)}</div>`;
      }
    });

  // Lead Scoring Form
  document
    .getElementById("score-form")
    .addEventListener("submit", async (e) => {
      e.preventDefault();
      const data = {
        lead_name: document.getElementById("score-name").value,
        budget: document.getElementById("score-budget").value,
        need: document.getElementById("score-need").value,
        urgency: document.getElementById("score-urgency").value,
      };

      const result = await fetchAI(
        "/api/score",
        data,
        e.submitter,
        "score-result",
      );
      if (result) {
        renderScore(result);
      }
    });

  // Helper: Simple Markdown-like formatter
  function formatText(text) {
    // Convert **bold** to <strong>
    let formatted = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    // Convert newlines to <br>
    formatted = formatted.replace(/\n/g, "<br>");
    return formatted;
  }

  // Helper: Render Score Visualization
  function renderScore(data) {
    const score = data.score;
    let color = "#ef4444"; // Red for low
    if (score >= 40) color = "#f59e0b"; // Orange for medium
    if (score >= 70) color = "#10b981"; // Green for high

    const html = `
            <div class="score-display">
                <div class="score-circle" style="border-color: ${color}; color: ${color};">
                    ${score}
                </div>
                <h3>Start Score</h3>
                <div class="score-details">
                    <p><strong>Conversion Probability:</strong> ${data.conversion_probability}</p>
                    <p style="margin-top: 0.5rem;"><strong>Reasoning:</strong> ${data.reasoning}</p>
                </div>
            </div>
        `;
    document.getElementById("score-result").innerHTML = html;
  }
});
