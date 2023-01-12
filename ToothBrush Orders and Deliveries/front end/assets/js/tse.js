/** Logic for embedding and controlling the application. */


import {
    init,
    AuthType,
    LiveboardEmbed,
}
    from "https://cdn.jsdelivr.net/npm/@thoughtspot/visual-embed-sdk/dist/tsembed.es.js";

//'https://unpkg.com/@thoughtspot/visual-embed-sdk/dist/tsembed.es.js';

// 1) - Set the tsURL to point to your ThoughtSpot instance.

// If you are using the free trial the URL will be like the following:

const tsMY3 = "https://my1.thoughtspot.cloud";

const my3Live = "bcbb109b-35cd-40fb-ba95-7cf87612ff7d";


/** Initializes the application with ThoughtSpot. */

const
    loadApp = () => {
        init({
            thoughtSpotHost : tsMY3,
            authType: AuthType.None,
        });

        document.getElementById("embed").innerHTML = "";
    }

const onLiveboard = () => {

    console.log('liveboard clicked');

    // Instantiate class for embedding a Liveboard

    const embed = new LiveboardEmbed("#embed",
        {
            frameParams: {},
            liveboardId: my3Live,
        });
    embed.render();
}

//Java script function to load quicksight html
function getpdf() {
    $('#embed').load('quicksight.html');
    return false;
}

//click
document.getElementById('liveboard-link').addEventListener('click', onLiveboard);
document.getElementById('quicksight-link').addEventListener('click', getpdf);


// Clears the embedded section.

const clearEmbed = () => {
        const div = document.getElementById("embed");
        div.innerHTML = "";
    }


// closes the modal element when the close is selected.

const closeModal = () => {
    const showDataElement = document.getElementById('show-data')
    showDataElement.style.display = 'none';
    // hide the box.

}

window.onload = loadApp;
//window.onload = onLiveboard;
setTimeout(function(){
	onLiveboard();
    }, 1000);
