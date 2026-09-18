// Navigation stays usable without JavaScript; enhance only after controls are wired.
const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
if (toggle && navigation) {
  const closeMenu = () => {
    toggle.setAttribute('aria-expanded', 'false');
    navigation.classList.remove('is-open');
  };
  toggle.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(expanded));
    navigation.classList.toggle('is-open', expanded);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      toggle.focus();
    }
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.site-header')) closeMenu();
  });
  navigation.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  matchMedia('(min-width: 761px)').addEventListener('change', closeMenu);
  toggle.hidden = false;
  document.documentElement.classList.add('menu-ready');
}
const copyButton = document.querySelector('.copy-handle');
if (copyButton && navigator.clipboard && window.isSecureContext) {
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    const status = document.querySelector('.copy-status');
    try {
      await navigator.clipboard.writeText(copyButton.dataset.copy);
      status.textContent = 'Copied! Find me on Discord as Warden314.';
    } catch {
      status.textContent = 'Select and copy Warden314 above to find me on Discord.';
    }
  });
}
