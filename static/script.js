function randomStyle() {
    const styles = ["star", "box", "wave", "mirror", "steps"];
    const random = styles[Math.floor(Math.random() * styles.length)];
    document.getElementById("style").value = random;
}

// Optional: Auto preview as user types
document.getElementById("text")?.addEventListener("input", () => {
    const preview = document.getElementById("preview");
    if (preview) preview.style.borderLeftColor = "#2575fc";
});
