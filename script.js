function getData() {
  fetch('http://127.0.0.1:8000/sql')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('data');
      container.innerHTML = '';
      data.forEach(item => {
        const element = document.createElement('p');
        element.innerText = `${item.id}. ${item.title}`;
        container.appendChild(element);
      });
    })
    .catch(error => console.error(error));
}



