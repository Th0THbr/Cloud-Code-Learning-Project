alert("JS is connected");

const pages = document.querySelectorAll("section");

const showPage = (pageID) => {
	pages.forEach(page => {
		page.style.display= "none";
		});
	document.getElementById(pageID).style.display ="block";
}


const tabActions = {
homePage: () => showPage("homePage"),
gamesPage: () => showPage("gamesPage"),
playersPage: () => showPage("playersPage"),
simfantPage: () => showPage("simfantPage"),
settPage: () => showPage("settPage")
};



const tabButtons= document.querySelectorAll(".tab-button");
tabButtons.forEach(button => {
	button.onclick = () => {
		tabActions[button.dataset.page]();
	};
});
