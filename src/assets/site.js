const toggle = document.querySelector('.nav-toggle');
const navigation = document.querySelector('#hoofdnavigatie');
const submenus = [...navigation.querySelectorAll('details')];

document.documentElement.classList.add('has-js');

function closeSubmenus() {
  for (const submenu of submenus) submenu.open = false;
}

toggle.addEventListener('click', () => {
  const isOpen = toggle.getAttribute('aria-expanded') === 'true';
  toggle.setAttribute('aria-expanded', String(!isOpen));
  if (isOpen) closeSubmenus();
});

for (const submenu of submenus) {
  submenu.addEventListener('toggle', () => {
    if (!submenu.open) return;
    for (const other of submenus) {
      if (other !== submenu) other.open = false;
    }
  });
}

navigation.addEventListener('click', (event) => {
  if (!event.target.closest('a')) return;
  closeSubmenus();
  toggle.setAttribute('aria-expanded', 'false');
});

document.addEventListener('click', (event) => {
  if (!navigation.contains(event.target)) closeSubmenus();
});

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  const openSubmenu = submenus.find((submenu) => submenu.open);
  if (openSubmenu) {
    openSubmenu.open = false;
    openSubmenu.querySelector('summary').focus();
  } else if (toggle.getAttribute('aria-expanded') === 'true') {
    toggle.setAttribute('aria-expanded', 'false');
    toggle.focus();
  }
});
