const swiper = new Swiper('.swiper',{
    mousewheel:true,
    direction: 'vertical',
    speed:1700,
    parallax:true
})
document.querySelectorAll('.header-content h1').forEach(e => {
	e.innerHTML = e.textContent.replace(/ (-|#|@){1}/g, s => s[1]+s[0]).replace(/(\S*)/g, m => {
		return m.replace(/\S(-|#|@)?/g, '<span class="letter">$&</span>')
	})
	e.querySelectorAll('.letter').forEach(function(l, i) {
		l.setAttribute('style', `z-index: -${ i }; transition-duration: ${ i/5 + 1 }s`)
	})
})

swiper.on('slideChange', function() {
	document.querySelectorAll('.header-content__slide').forEach(function(e, i) {
		return swiper.activeIndex === i ? e.classList.add('active') : e.classList.remove('active')
	})
})


/**
 * нижняя прокрутка
 */
const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
if (mediaQuery && !mediaQuery.matches) {
	const tagScroller = document.querySelector(".tag-scroller");
	const allTags = tagScroller.querySelectorAll("li");
	
	function createElement(tagName, className = "") {
		const elem = document.createElement(tagName);
		elem.className = className;
		return elem;
	}

	function scrollersFrom(elements, numColumns = 2) {
		const fragment = new DocumentFragment();
		elements.forEach((element, i) => {
			const column = i % numColumns;
			const children = fragment.children;
			if (!children[column]) fragment.appendChild(createElement("ul", "tag-list"));
			children[column].appendChild(element);
		});
		return fragment;
	}

	const scrollers = scrollersFrom(allTags, 2);
	tagScroller.innerHTML = "";
	tagScroller.appendChild(scrollers);
	addScrolling();


	function addScrolling() {
		tagScroller.classList.add("scrolling");
		document.querySelectorAll(".tag-list").forEach((tagList) => {
			const scrollContent = Array.from(tagList.children);
			scrollContent.forEach((listItem) => {
				const clonedItem = listItem.cloneNode(true);
				clonedItem.setAttribute("aria-hidden", true);
				tagList.appendChild(clonedItem);
			});
			tagList.style.setProperty("--duration", (tagList.clientWidth / 100) + "s");
		});
	}
}