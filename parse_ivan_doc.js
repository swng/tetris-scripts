// Script for scraping Ivan(28283)'s Comprehensive Opener Database into js object
// https://docs.google.com/document/d/e/2PACX-1vRPRV-vrgoIx3EVGxjPqeKKtnry2Sr1l-XU_vx3Tumx-kA4Rmh117T8iAskAh0QTI9ZFhOAkDN_3v10/pub
// load this published googledoc site
// run this script in console

// Note! You will need to figure out the correct class name first and edit L24 accordingly!

// ok first let's fix all the googledoc middleman links
const links = document.querySelectorAll('a');

links.forEach(link => {
    let old_url = link.href;
    if (old_url.includes("url?q=")) { // this should capture all the googledoc middleman links probably maybe
        let url = new URL(old_url);
        let actualLink = url.searchParams.get('q');

        link.setAttribute('href', actualLink);

    }
})

// now let's parse it

let bigList = document.getElementsByClassName("c27 c30 doc-content")[0].childNodes;
// ok the exact class name seems to change around but you should be able to figure it out via inspect element - just the element with all the content in it!!!

let opener_list = [];
let categories = [];
let rich_categories = {};
let last_category_primary = "";
let last_category_secondary = "";

for(i = 0; i < bigList.length - 7; i++) {  // last title is followed by like 7 more lines
    if (bigList[i].id) {
        let next = bigList[i+1].textContent;
        if (next.includes("SEARCH") || next.includes("Sources")) {
            // console.log(i, bigList[i].textContent);
            let nextOpener = {name: bigList[i].textContent};
            let parsed = [];
            let endOpenerParse = false;
            for(j = i+1; !endOpenerParse && j < bigList.length; j++) { // while not at end of [this current opener] and alsonot at end of the whole document
                let line = bigList[j].cloneNode(true);
                    if (line && !line.id) {
                        // console.log(line.textContent);
                        // gonna be leaving the data in its raw HTML form, preserving links and formatting i g

                        // includes may fuckup categorization (e.g. if a category name is within the text of another section. This seems to only happen with the Notes section including misc text, so Notes is the first if clause)
                        // startswith would not really have this issue, but using includes just in case there's a leading space or something, idk, idk
                        if (line.textContent.includes("Notes")) {
                            nextOpener["Notes"] = [line.outerHTML];
                            parsed.push("Notes");
                        }
                        else if (line.textContent.includes("SEARCH")) {
                            nextOpener["SEARCH"] = [line.outerHTML];
                            parsed.push("SEARCH");
                        }
                        else if (line.textContent.includes("Sources")) {
                            nextOpener["Sources"] = [line.outerHTML];
                            parsed.push("Sources");
                        }
                        else if (line.textContent.includes("PC Chance")) {
                            nextOpener["PC Chance"] = [line.outerHTML];
                            parsed.push("PC Chance");
                        }
                        else if (line.textContent.includes("Dependencies")) {
                            nextOpener["Dependencies"] = [line.outerHTML];
                            parsed.push("Dependencies");
                        }
                        else if (line.textContent.includes("Cover")) {
                            nextOpener["Cover"] = [line.outerHTML];
                            parsed.push("Cover");
                        }
                        else if (line.textContent.includes("Fumen")) {
                            nextOpener["Fumen"] = [line.outerHTML];
                            parsed.push("Fumen");
                        }
                        else { // probably the second line of a category
                            let category = parsed.slice(-1)[0]; // last parsed category
                            if (category) {
                                if (category == "Fumen") { // special cases at the end
                                    nextOpener["Image"] = [line.outerHTML];
                                    parsed.push("Image");
                                }
                                else if (category == "Image") { // special cases at the end
                                    nextOpener["extra Notes"] = [line.outerHTML];
                                    parsed.push("extra Notes");
                                }
                                else nextOpener[category].push(line.outerHTML); // this line goes into the category of prev line
                            }
                            else {throw new Error("ummm");} // should never happen. Parsing only begins in the first place if the first thing is parsable (search or sources). And the first moment parsing begins, parsed array is populated.

                        }
                    }
                else { endOpenerParse = true; }
            }
            nextOpener["tag_primary"] = last_category_primary;
            nextOpener["tag_secondary"] = last_category_secondary;
            if (opener_list.length == 0) {
                // this is actually the TOC, not an opener.
                let href_regex = /href="(?:#)?(.*?)"/g;
                for (let category of nextOpener["Sources"]) {
                    let match;
                    while (match = href_regex.exec(category)) {
                        categories.push(match[1]);
                    }
                }
            }
            opener_list.push(nextOpener);
        }
        else if (categories.includes(bigList[i].id)) {
            let category = bigList[i].textContent;
            if (category.startsWith("[1st Bag") || category == "Sources" || category == "Extra" || category.startsWith("THE GARAGE")) {
                last_category_primary = category;
            }
            else {
                last_category_secondary = category;
            }

            rich_categories[bigList[i].id] = [last_category_primary, last_category_secondary];
        }
    }
}

opener_list[0]["categories"] = rich_categories;

// let's throw the current time into the object, uh, inside the worthless Contents object
let a = new Date();
opener_list[0]["timestamp"] = a.toISOString();

// hopefully opener_list array is populated with opener objects!

// export!!!!

const jsonData = JSON.stringify(opener_list);

const blob = new Blob([jsonData], { type: 'application/json' });

const link = document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download = 'data.json';
link.click();