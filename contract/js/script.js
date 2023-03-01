const btnMenu = document.querySelector('.button-menu');
const sitenav = document.querySelector('.sitenav');
const sHeader = document.querySelector('.site-header')

btnMenu.addEventListener('click', ()=> {
  if (!sitenav.classList.contains('open')) {
    sitenav.classList.add('open')
    btnMenu.innerHTML = `<img class="close" src="img/close.svg" alt="menu-icon" width="44" height="44">`
  } else {
    sitenav.classList.remove('open')
    btnMenu.innerHTML = `<img class="menu" src="img/menu.svg" alt="menu-icon" width="48" height="48">`
  }
})