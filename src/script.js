function extractEmails() {
  let text = document.getElementById('textArea').value;
  fetch('http://localhost:5000/extract_emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text: text }),
  })
    .then((response) => response.json())
    .then((data) => {
      let emailsList = document.getElementById('emailsList');
      emailsList.innerHTML = '';
      data?.emails?.forEach(function (email) {
        let li = document.createElement('li');
        li.appendChild(document.createTextNode(email));
        emailsList.appendChild(li);
      });
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}
