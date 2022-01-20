window.onload = function () {
    let how_i_die_text = document.getElementById("how_to_die_text");
    let how_i_die_button = document.getElementById("how_i_die_button");
    
    function how_i_die() {
        eel.get_death()(function(ret) {
            how_i_die_text.innerHTML = ret;
        })
    }

    // Returns random "How I Die" message from python backend when button is clicked.
    how_i_die_button.addEventListener("click", how_i_die);
}