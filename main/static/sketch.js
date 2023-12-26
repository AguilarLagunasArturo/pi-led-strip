let pg;
let tree;

let canvas_w;
let canvas_h;
let canvas_half_w;
let canvas_half_h;

let tree_w;
let tree_h;
let tree_d;

let levels;
let mouse_diameter;
let sphere_diameter;
let spheres = [];

let current_state = 1;
let DEFAULT_STATUS = [
    [200, 200, 200],
    [200, 0, 0],
    [0, 200, 0],
    [0, 0, 200]
];

function preload() {
    tree = loadModel('/static/tree.obj', true);
}

function mouseClicked() {
    let hexColor = $('#colorPicker').val();
    let rgbColor = hexToRgb(hexColor);
    console.log(mouseX, mouseY, rgbColor)
    collitions = getSphereCollitions(spheres, 30, rgbColor);
    if (collitions.length > 0) {
        // Define the action
        let actionData = {
            action: "p5_click",
            leds: collitions,
            color: rgbColor
        };

        // Send the action data to Flask
        fetch('/execute-action', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(actionData),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            console.log('Data:', actionData);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
}

function hexToRgb(hex) {
    var r = parseInt(hex.slice(1, 3), 16);
    var g = parseInt(hex.slice(3, 5), 16);
    var b = parseInt(hex.slice(5, 7), 16);
    return [r, g, b];
}

function toggleState() {
    let ix = 0;
    let curr_rgb = DEFAULT_STATUS[current_state];
    current_state = (current_state + 1) % 4;
    console.log(curr_rgb);
    for (let i = 0; i < levels.length; i++) {
        for (let j = 0; j < levels[i]; j++) {
            spheres[ix].updateColor(curr_rgb[0], curr_rgb[1], curr_rgb[2]);
            ix += 1;
        }
    }
}


function setup() {
    levels = [20, 10, 10, 10, 10, 5, 5, 5, 5, 5, 4, 3, 3, 3, 2];
    mouse_diameter = 60;
    sphere_diameter = 6;

    let ix = 0;
    for (let i = 0; i < levels.length; i++) {
        for (let j = 0; j < levels[i]; j++) {
            spheres.push(new xmassSphere(sphere_diameter, ix));
            ix += 1;
        }
    }

    tree_w = 185; // 262;
    tree_h = 185; // 208;
    tree_d = 350; // 478;

    canvas_w = screen.availWidth * (1-0.85);
    canvas_h = screen.availHeight * (1-0.5);
    canvas_half_w = canvas_w/2;
    canvas_half_h = canvas_h/2;
    createCanvas(canvas_w, canvas_h, WEBGL);
}

function draw() {
    background(255, 255, 255);
    noStroke();

    push();
    translate(-canvas_half_w, -canvas_half_h, 0)
    stroke(0);
    noFill();
    ellipse(mouseX, mouseY, mouse_diameter, mouse_diameter);
    pop();

    rotateX(PI/2);
    let alpha = frameCount * 0.005;
    rotateZ(alpha);

    push()
    fill(87, 227, 137);
    // noStroke();
    stroke(0);
    // strokeWeight(0.5);
    scale(2);
    model(tree);
    pop()
    noFill();

//    push()
//    stroke(0);
//    box(tree_w, tree_h, tree_d);
//    pop()

    let ix = 0;
    let theta;
    let cartesian_x;
    let cartesian_y;
    let cartesian_x_projection;
    for (let i = 0; i < levels.length; i++) {
        for (let j = 0; j < levels[i]; j++) {
            // console.log( (j+1)/levels[i] );
            push();
            // stroke(0);
            translate(0, 0, 12);
            theta = (TWO_PI/levels[i]) * j;
            rotateZ(theta); // (j+1)/levels[i]
            cartesian_x = tree_w/2 - i*(tree_h*0.028);
            cartesian_y = -tree_d/2 + i * (tree_d/15);
            cartesian_x_projection = cartesian_x * cos(theta+alpha)
            translate(
                cartesian_x,
                0,
                cartesian_y
            );
            // noStroke();
            spheres[ix].display();
            spheres[ix].updateProjection(
                cartesian_x_projection+canvas_half_w,
                cartesian_y*-1 + canvas_half_h
            );
            // console.log(cartesian_x_projection+canvas_half_w, cartesian_y*-1 + canvas_half_h);
            spheres[ix].x = cartesian_x_projection+canvas_half_w;
            spheres[ix].y = cartesian_y*-1 + canvas_half_h;
            // console.log(spheres[ix].x, spheres[ix].y);
            pop();
            ix += 1;
        }
    }
}


class xmassSphere {
        constructor(diameter, id) {
        this.diameter = diameter;
        this.id = id;
        this.x = 0;
        this.y = 0;
        this.color = [245, 194, 17];
    }

    updateProjection(x, y) {
        this.x = x;
        this.x = y;
    }

    updateColor(r, g, b) {
        this.color = [r, g, b]
    }

    display() {
        fill(this.color[0], this.color[1], this.color[2]);
        sphere(this.diameter);
    }

    getId() {
        return this.id;
    }
}

function getSphereCollitions(sphere_array, collition_threshold, newColor) {
    let sphere_collitions = []
    let point_x = mouseX;
    let point_y = mouseY;

    for (var i = 0; i < sphere_array.length; i++) {
        let d = sqrt(pow((sphere_array[i].x - point_x), 2) + pow(sphere_array[i].y - point_y, 2))
        if (d <= collition_threshold) {
            sphere_collitions.push(sphere_array[i].getId());
            sphere_array[i].updateColor(newColor[0], newColor[1], newColor[2]);
            console.log("[+] Collided: " + sphere_array[i].getId());
        }
    }
    return sphere_collitions
}
