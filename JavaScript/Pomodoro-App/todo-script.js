const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");
const completedCounter = document.getElementById("completed")

function addTask() {
    const task = inputBox.value.trim();
    if (!task) {
        alert("Please write down a task");
        return;
    }

    const li = document.createElement("li");
    li.innerHTML = 
        `<label>
            <input type="checkbox">
            <span>${task}</span>
        </label>
        <button class="edit-btn">Edit</button>
        <button class="delete-btn">Delete</button>
        `;

    listContainer.appendChild(li);
    inputBox.value = "";

    const checkbox = li.querySelector("input");
    const editBtn = li.querySelector(".edit-btn");
    const taskSpan = li.querySelector("span");
    const deleteBtn = li.querySelector(".delete-btn");

    checkbox.addEventListener("click", function () {
        li.classList.toggle("completed", checkbox.checked);
        updateCounters();

        // Change Delete/Edit Buttons
        if(checkbox.checked === true) {
            editBtn.style.cssText = `background-color: grey; color: white;`;
            deleteBtn.style.cssText = `background-color: grey; color: white;`;
        } else {
            editBtn.style.cssText = `background-color: white; color: grey;`;
            deleteBtn.style.cssText = `background-color: white; color: grey;`;
        }
    });

    editBtn.addEventListener("click", function () {
        const update = prompt("Edit task:", taskSpan.textContent);
        if (update !== null) {
            taskSpan.textContent = update;
            li.classList.remove("completed");
            checkbox.checked = false;
            updateCounters();

            // Change Delete/Edit Buttons
            editBtn.style.cssText = `background-color: white; color: grey;`;
            deleteBtn.style.cssText = `background-color: white; color: grey;`;
        }
    });

    const completedCounter = document.getElementById("completed-counter");
    const uncompletedCounter = document.getElementById("uncompleted-counter");

    function updateCounters() {
        const completedTasks = document.querySelectorAll(".completed").length;
        const uncompletedTasks = document.querySelectorAll("li:not(.completed)").length;

        completedCounter.textContent = completedTasks;
        uncompletedCounter.textContent = uncompletedTasks;
    }

    updateCounters();

    deleteBtn.addEventListener("click", function () {
        if (confirm("Are you sure you want to delete this task?")) {
            li.remove();
            updateCounters();
        }
    });
}