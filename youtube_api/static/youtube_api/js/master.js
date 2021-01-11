const search_form_box = document.getElementById('search_box');
const search_position = search_form_box.getBoundingClientRect();
const search_position_top = search_position.top;

let window_scroll_position = window.pageYOffset;

window.addEventListener('scroll', scroll_position);

function scroll_position() {
  console.log(search_position_top);
}
