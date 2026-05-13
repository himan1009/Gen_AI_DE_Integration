document.addEventListener('DOMContentLoaded', () => {

    const todoInput = document.getElementById('todo-input');
    const addTodoBtn = document.getElementById('add-todo-btn');
    const todoList = document.getElementById('todo-list');

    let todos = JSON.parse(localStorage.getItem('todos')) || [];


    function saveTodos() {
        localStorage.setItem('todos', JSON.stringify(todos));
    }


    function renderTodos() {

        todoList.innerHTML = '';

        todos.forEach((todo, index) => {

            const listItem = document.createElement('li');

            listItem.innerHTML = `
                <span class='todo-text ${todo.completed ? 'completed' : ''}'>
                    ${todo.text}
                </span>

                <div class='actions'>
                    <button class='complete-btn' data-index='${index}'>
                        ${todo.completed ? 'Undo' : 'Complete'}
                    </button>

                    <button class='edit-btn' data-index='${index}'>
                        Edit
                    </button>

                    <button class='delete-btn' data-index='${index}'>
                        Delete
                    </button>
                </div>
            `;

            todoList.appendChild(listItem);
        });
    }


    function addTodo() {

        const text = todoInput.value.trim();

        if (text !== '') {

            todos.push({
                text: text,
                completed: false
            });

            todoInput.value = '';

            saveTodos();

            renderTodos();
        }
    }


    function deleteTodo(index) {

        todos.splice(index, 1);

        saveTodos();

        renderTodos();
    }


    function toggleComplete(index) {

        todos[index].completed = !todos[index].completed;

        saveTodos();

        renderTodos();
    }


    function editTodo(index) {

        const oldText = todos[index].text;

        const listItem = todoList.children[index];

        const spanElement = listItem.querySelector('.todo-text');

        const actionsDiv = listItem.querySelector('.actions');

        spanElement.style.display = 'none';

        actionsDiv.style.display = 'none';


        const editInput = document.createElement('input');

        editInput.type = 'text';

        editInput.className = 'edit-input';

        editInput.value = oldText;

        listItem.prepend(editInput);

        editInput.focus();


        editInput.addEventListener('keypress', (e) => {

            if (e.key === 'Enter') {

                const newText = editInput.value.trim();

                if (newText !== '') {

                    todos[index].text = newText;

                    saveTodos();

                    renderTodos();

                } else {

                    renderTodos();
                }
            }
        });


        editInput.addEventListener('blur', () => {

            const newText = editInput.value.trim();

            if (newText !== '' && newText !== oldText) {

                todos[index].text = newText;

                saveTodos();
            }

            renderTodos();
        });
    }


    addTodoBtn.addEventListener('click', addTodo);


    todoList.addEventListener('click', (e) => {

        if (e.target.classList.contains('delete-btn')) {

            const index = e.target.dataset.index;

            deleteTodo(index);

        } else if (e.target.classList.contains('complete-btn')) {

            const index = e.target.dataset.index;

            toggleComplete(index);

        } else if (e.target.classList.contains('edit-btn')) {

            const index = e.target.dataset.index;

            editTodo(index);
        }
    });


    renderTodos();
});