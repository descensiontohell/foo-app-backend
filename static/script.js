function loadPage(pageName) {
  fetch(`/api/${pageName}`)
    .then((response) => response.text())
    .then((content) => {
      document.getElementById('app').innerHTML = content
      history.pushState({}, null, `/${pageName}`)
    })
    .catch((error) => console.error(error))
}

document.addEventListener('click', (event) => {
  const target = event.target
  if (target.tagName === 'A') {
    event.preventDefault() // Prevent default link behavior

    const href = target.getAttribute('href')
    const pageName = href.slice(1) // Get the page name from the href attribute
    loadPage(pageName)
  }
})

// Load initial page on startup
function refresh() {
  const initialPageName = location.pathname.slice(1)
  if (initialPageName) {
    loadPage(initialPageName)
  } else {
    loadPage('home')
  }
}

function submitNewItemForm() {
  const newItemForm = document.getElementById('new__item__form')

  const data = new URLSearchParams(new FormData(newItemForm))

  fetch('/api/items/', {
    method: 'post',
    body: data,
  }).then((response) => (refresh()));
}

refresh()
