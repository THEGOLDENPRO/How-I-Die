window.onload = function () {
    let how_i_die_text = document.getElementById("how_to_die_text");
    how_i_die_author = document.getElementById("how_i_die_author")
    let how_i_die_button = document.getElementById("how_i_die_button");
    
    function how_i_die() {
        eel.get_death()(function(ret) {
            how_i_die_text.innerText = ret[0];
            how_i_die_author.innerText = ret[1];
        })
    }

    // Returns random "How I Die" message from python backend when button is clicked.
    how_i_die_button.addEventListener("click", how_i_die);
}