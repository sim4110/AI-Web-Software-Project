/*
    작성자: 이은총
    비고: 네비게이션 바 JS
*/

const toggleBtn = document.querySelector('.navbar__toggleBtn');
const menu = document.querySelector('.navbar__menu');
const account = document.querySelector('.navbar__account');

toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
    account.classList.toggle('active');
});
