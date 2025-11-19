
const searchInput = document.getElementById('search');
const taskList = document.getElementById('task-list');

searchInput.addEventListener('input', function() {
    const filter = searchInput.value.toLowerCase();
    const tasks = taskList.getElementsByTagName('li');

    for (let i = 0; i < tasks.length; i++) {
        const span = tasks[i].getElementsByTagName('span')[0];
        const text = span.textContent.toLowerCase();
        if (text.includes(filter)) {
            tasks[i].style.display = '';
        } else {
            tasks[i].style.display = 'none';
        }
    }
});

const deleteButtons = document.querySelectorAll('.delete-btn');

deleteButtons.forEach(button => {
    button.addEventListener('click', function(event) {
        const confirmed = confirm("Are you sure you want to delete this task?");
        if (!confirmed) {
            event.preventDefault(); 
        }
    });
});
