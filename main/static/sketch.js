let pg;
let tree;

let canvas_w;
let canvas_h;
let canvas_half_w;
let canvas_half_h;

function preload() {
    tree = loadModel('/static/tree.obj', true);
}

//function mouseClicked() {
//    // Define the action
//    let actionData = { action: "p5_click" };
//
//    // Send the action data to the Flask server
//    fetch('/execute-action', {
//        method: 'POST',
//        headers: {
//            'Content-Type': 'application/json',
//        },
//        body: JSON.stringify(actionData),
//    })
//    .then(response => response.json())
//    .then(data => {
//        console.log('Success:', data);
//    })
//    .catch((error) => {
//        console.error('Error:', error);
//    });
//}

function setup() {
    canvas_w = screen.availWidth * (1-0.2);
    canvas_h = screen.availHeight * (1-0.2);
    canvas_half_w = canvas_w/2;
    canvas_half_h = canvas_h/2;
    createCanvas(canvas_w, canvas_h, WEBGL);
    // pg = createGraphics(400, 250);
}

function draw() {
    background(255, 255, 255);

    translate(-canvas_half_w, -canvas_half_h, 0)
    fill(32, 32, 32);
    noStroke();
    ellipse(mouseX, mouseY, 60, 60);
    translate(canvas_half_w, canvas_half_h, 0)

//
//    pg.background(51);
//    pg.noFill();
//    pg.stroke(255);
//    pg.ellipse(mouseX - 150, mouseY - 75, 60, 60);

    //Draw the offscreen buffer to the screen with image()
    //image(pg, 150, 75);

    // translate(canvas_half_h, canvas_half_h, 0)
    //rotateZ(frameCount * 0.01);
    //rotateX(frameCount * 0.01);
    rotateX(PI/2);
    rotateZ(frameCount * 0.01);
    fill(20, 200, 80);
    stroke(0);
    model(tree);
    noFill()
    box(262/2, 208/2, 478/2)
}
