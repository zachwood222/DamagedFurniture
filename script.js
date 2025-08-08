
document.getElementById("damageForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    const itemName = document.getElementById("itemName").value;
    const damageDesc = document.getElementById("damageDesc").value;
    const hoursWorked = document.getElementById("hoursWorked").value;
    const res = await fetch("/add", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ item: itemName, description: damageDesc, hours: parseFloat(hoursWorked) })
    });
    if (res.ok) {
        document.getElementById("alertBox").innerText = "Item added!";
        loadTable();
    }
});

async function loadTable() {
    const res = await fetch("/items");
    const items = await res.json();
    const tbody = document.querySelector("#damageTable tbody");
    tbody.innerHTML = "";
    items.forEach(item => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.item}</td>
            <td>${item.description}</td>
            <td>${item.hours}</td>
            <td>${item.status}</td>
            <td><button onclick="resolveItem(${item.id})">Mark Resolved</button></td>
        `;
        tbody.appendChild(row);
    });
}

async function resolveItem(id) {
    await fetch(`/resolve/${id}`, { method: "POST" });
    loadTable();
}

window.onload = loadTable;
