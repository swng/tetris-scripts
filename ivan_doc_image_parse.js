// from data.json of parsed ivan doc, grab the images, and parse all of them
// outputs data-2.json, everything the same except Image section includes array of fumens instead of html with image links

const { decoder, encoder, Field } = require('tetris-fumen');

var { Image, createCanvas } = require('canvas');
const { loadImage } = require('canvas');

const fs = require('fs');

function rgb2hsv(r, g, b) {
	let v = Math.max(r, g, b),
		c = v - Math.min(r, g, b);
	let h = c && (v == r ? (g - b) / c : v == g ? 2 + (b - r) / c : 4 + (r - g) / c);
	return [60 * (h < 0 ? h + 6 : h), v && c / v, v];
}

function nearestColor(h, s, v) {
	if (inRange(s, 0, 1) && (inRange(v, 133, 135) || inRange(v, 63, 88))) return 'X'; // attempted manual override specifically for four.lol idk
	if (inRange(h, 220, 225) && inRange(s, 0, 0.2) && v == 65) return '.';

	if (s <= 0.2 && v / 2.55 >= 55) return 'X';
	if (v / 2.55 <= 55) return '.';

	if (inRange(h, 0, 16) || inRange(h, 325, 360)) return 'Z';
	else if (inRange(h, 16, 40)) return 'L';
	else if (inRange(h, 39, 70)) return 'O';
	else if (inRange(h, 70, 149)) return 'S';
	else if (inRange(h, 149, 200)) return 'I';
	else if (inRange(h, 200, 266)) return 'J';
	else if (inRange(h, 266, 325)) return 'T';
	return '.';
}

function inRange(x, min, max) {
	return x >= min && x <= max;
}

function median(values) {
	// if this is too computationally expensive maybe switch to mean
	if (values.length === 0) throw new Error('No inputs');

	values.sort(function (a, b) {
		return a - b;
	});

	var half = Math.floor(values.length / 2);

	if (values.length % 2) return values[half];

	return (values[half - 1] + values[half]) / 2.0;
}


let rawdata = fs.readFileSync('data.json');
let openers = JSON.parse(rawdata);
// console.log(openers);

async function fumenify_images() {
    for (i = 1; i < openers.length; i++) {
        if ("Image" in openers[i]) {
            let imagesHTML = openers[i]["Image"][0];
            console.log(i);
            // console.log(imagesHTML);

            let fumens = [];

            const imgSrcRegex = /<img.*?src="(.*?)"/g;

            const imgSrcList = [];
            let match;

            while ((match = imgSrcRegex.exec(imagesHTML)) !== null) {
                imgSrcList.push(match[1]);
            }

            // console.log(imgSrcList);

            for (imgSrc of imgSrcList) {
                // console.log(imgSrc);

                const myimg = await loadImage(imgSrc).then((image) => {
                    // console.log(imgSrc);
                    // console.log(image.width, image.height);
                    scale = image.width / 10.0;
                    x = 10;
                    y = Math.min(Math.round(image.height / scale), 22);
                    // console.log(x, y);

                    const canvas = createCanvas(image.width, image.height);
                    const ctx = canvas.getContext('2d');

                    ctx.drawImage(image, 0, 0, image.width, image.height);
                    var data = Object.values(ctx.getImageData(0, 0, image.width, image.height).data);
                    // console.log(data)

                    var nDat = [];
                    for (let row = 0; row < y; row++) {
                        for (let col = 0; col < 10; col++) {
                            // get median value of pixels that should correspond to [row col] mino

                            let minoPixelsR = [];
                            let minoPixelsG = [];
                            let minoPixelsB = [];

                            for (
                                let pixelRow = Math.floor(row * scale);
                                pixelRow < row * scale + scale;
                                pixelRow++
                            ) {
                                for (
                                    let pixelCol = Math.floor(col * scale);
                                    pixelCol < col * scale + scale;
                                    pixelCol++
                                ) {

                                    let index = (pixelRow * image.width + pixelCol) * 4;
                                    minoPixelsR.push(data[index]);
                                    minoPixelsG.push(data[index + 1]);
                                    minoPixelsB.push(data[index + 2]);
                                }
                            }

                            let medianR = median(minoPixelsR);
                            let medianG = median(minoPixelsG);
                            let medianB = median(minoPixelsB);
                            var hsv = rgb2hsv(medianR, medianG, medianB);
                            // console.log(hsv, nearestColor(hsv[0], hsv[1], hsv[2])); // debugging purposes
                            nDat.push(nearestColor(hsv[0], hsv[1], hsv[2]));
                        }
                    }

                    FieldString = '';
                    for (rowIndex = 0; rowIndex < y; rowIndex++) {
                        for (colIndex = 0; colIndex < 10; colIndex++) {
                            index = rowIndex * 10 + colIndex;
                            temp = nDat[index];

                            if (temp == '.') FieldString += '_'
                            else FieldString += temp;
                        }
                    }

                    const pages = [];
                    pages.push({
                        field: Field.create(FieldString),
                    });
                    let fumen = encoder.encode(pages);

                    fumens.push(fumen);

                });
            
            }

            // console.log(fumens);
            openers[i]["Image"][0] = fumens;

            
        }
            
    }
    let data = JSON.stringify(openers);

    fs.writeFileSync('data-2.json', data);
}

fumenify_images();