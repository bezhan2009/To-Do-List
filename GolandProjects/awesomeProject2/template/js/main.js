let savedBlockHtml = ''; // Глобальная переменная для сохранения HTML блока

document.addEventListener('DOMContentLoaded', () => {
    const headerNavMenu = document.querySelector('.header');
    let lastScrollTop = 0;

    window.addEventListener('scroll', () => {
        let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScroll > lastScrollTop) {
            // Скролл вниз
            headerNavMenu.classList.remove('visible');
            headerNavMenu.classList.add('hidden');
        } else {
            // Скролл вверх
            headerNavMenu.classList.remove('hidden');
            headerNavMenu.classList.add('visible');
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    });

    document.getElementById('documentation').addEventListener('click', function() {
        window.location.href = 'documentation.html';
    });

    document.getElementById('support').addEventListener('click', function() {
        window.location.href = 'https://t.me/ExploreInspire';
    });

    // Функция для получения и отображения задач
    function fetchTasks() {
        const apiUrl = "http://localhost:8080/tasks"; // замените на ваш URL

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const tasksContainer = document.querySelector(".my-tasks");

                if (data.length === 0) {
                    tasksContainer.innerHTML = "";
                    // Если нет задач, отображаем сообщение
                    const noTasksMessage = document.createElement("div");
                    noTasksMessage.classList.add("no-tasks-message");
                    noTasksMessage.textContent = "У вас нет задач";
                    tasksContainer.appendChild(noTasksMessage);
                } else {
                    tasksContainer.innerHTML = '<h1 class="my-tasks-text">Мои задачи</h1>';

                    // Если есть задачи, добавляем их в контейнер
                    data.forEach(task => {
                        const taskElement = document.createElement("div");
                        taskElement.classList.add("task");
                        taskElement.innerHTML = `
                        <button class="delete-btn">&times;</button>
                        <h2>${task.title}</h2>
                        <h3>
                            <pre>${task.content}</pre>
                        </h3>
                    `;

                        // Добавляем обработчик удаления для каждой новой задачи
                        taskElement.querySelector(".delete-btn").addEventListener("click", function () {
                            const task = this.closest(".task"); // Найти ближайший блок .task
                            task.classList.add("fade-out"); // Добавляем класс для анимации исчезновения
                            setTimeout(() => {
                                task.remove(); // Удалить блок из DOM после анимации
                                // Проверяем, если теперь нет задач, отображаем сообщение
                                if (tasksContainer.querySelectorAll(".task").length === 0) {
                                    tasksContainer.innerHTML = '';

                                    const noTasksMessage = document.createElement("div");
                                    noTasksMessage.classList.add("no-tasks-message");
                                    noTasksMessage.textContent = "У вас нет задач";
                                    tasksContainer.appendChild(noTasksMessage);
                                }
                            }, 200); // Задержка должна соответствовать времени анимации
                        });

                        tasksContainer.appendChild(taskElement);
                    });
                }
            })
            .catch(error => console.error("Ошибка при получении данных:", error));
    }

    // Заполняем задачи при загрузке страницы
    fetchTasks();

    // Сохранение задачи
    const saveButton = document.getElementById("save_task");
    const cancelButton = document.getElementById("cancel_task");

    saveButton.addEventListener("click", function() {
        shutTasks()
        const title = document.getElementById("title").value;
        const content = document.getElementById("content").value;

        if (title && content) {
            const task = {
                title: title,
                content: content
            };

            fetch("http://localhost:8080/tasks/create", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(task)
            })
                .then(response => {
                    if (response.ok) {
                        document.getElementById("title").value = "";
                        document.getElementById("content").value = "";

                        // Обновляем список задач после добавления новой задачи
                        fetchTasks();
                    } else {
                        alert("Failed to save task.");
                    }
                })
                .catch(error => {
                    console.error("Error:", error);
                });
        } else {
            alert("Please fill out both fields.");
        }
    });

    cancelButton.addEventListener("click", function() {
        document.getElementById("title").value = "";
        document.getElementById("content").value = "";
    });
});

// Функция для переключения меню
function toggleMenu() {
    let menu = document.querySelector('.header-nav-menu');
    menu.classList.toggle('show');
}

function shutTasks() {
    const ourBlock = document.querySelector(".create-task");
    const special_styles = document.getElementById("special-styles")

    special_styles.innerHTML = `
       .create-task {
           transform: scale(0, 0)
       }
       
       .black_block {
           transform: scale(0, 0)
       }
       `
}

function showTasks() {
    const restoredBlock = document.querySelector(".create-task");

    const special_styles = document.getElementById("special-styles")

    special_styles.innerHTML = `
       .create-task {
           transform: scale(1, 1)
       }
       
       .black_block {
           transform: scale(1, 1)
       }
       `
    // Очистка сохранённого HTML
    savedBlockHtml = '';
}
