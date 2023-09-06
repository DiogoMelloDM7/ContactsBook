function excluirContato(contatoId) {
    if (confirm("Tem certeza que deseja excluir este contato?")) {
        const csrftoken = getCookie('csrftoken');
        fetch(`/excluirContato/${contatoId}`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": csrftoken,
            },
        })
        .then((response) => {
            if (response.ok) {
                location.reload(); // Atualiza a página após excluir o item
            } else {
                alert("Ocorreu um erro ao excluir o contato.");
            }
        })
        .catch((error) => {
            console.error("Erro na solicitação AJAX:", error);
        });
    }
}

function getCookie(name) {
let cookieValue = null;
if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Verifica se o cookie começa com o nome do token CSRF
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}