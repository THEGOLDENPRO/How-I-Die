window.onload = function () {
    let how_i_die_text = document.getElementById("how_to_die_text");

    const how_i_die_deaths = ["You died from eating a bowl of black pudding.", 
    "You died from swinging a baseball bat so hard that it ruptured your bladder.", 
    "You died from a monkey bite."];
    
    function how_i_die() { // Returns random "How I Die" message.
        const random_num = Math.floor(Math.random()*how_i_die_deaths.length);
        const message = how_i_die_deaths[random_num];
        how_i_die_text.innerHTML = message;
    }
    
    how_i_die_text.addEventListener("click", how_i_die);
}