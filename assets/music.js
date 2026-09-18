// Players load only when requested. The ordinary music link is always available.
document.querySelectorAll('[data-load-player]').forEach(button => {
  button.hidden = false;
  button.addEventListener('click', () => {
    const container = button.closest('.music-player');
    const template = container.querySelector('template');
    const slot = container.querySelector('.music-player-slot');
    if (slot.childElementCount) return;
    slot.append(template.content.cloneNode(true));
    button.disabled = true;
    button.textContent = 'Player requested';
    container.querySelector('[role="status"]').textContent =
      'If the player is unavailable, use the Listen link above.';
  });
});
