let data;
let cubes;

let xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        data = JSON.parse(this.responseText);
        //document.innerHTML = data.cubes[0].state;
        //let 0=no plant 1=ok 2=need water 3=disease
        document.innerHTML = data.cubes.length
        for (let i=0; i < data.cubes.length; i++) {
            document.innerHTML = data.cubes[i].row;
            document.innerHTML = data.cubes[i].col;
            document.innerHTML = data.cubes[i].stat;
            if (data.cubes[i].stat == 0) {
                //document.getElementById("r" + data.cubes[i].row + "c" + cubes[i].col).remove('grid-item-yellow');
                document.getElementById("r" + data.cubes[i].row+ "c" + data.cubes[i].col).className = 'grid-item';
            } else if (data.cubes[i].stat == 1) {
                document.getElementById("r" + data.cubes[i].row+ "c" + data.cubes[i].col).className = 'grid-item-green';
            } else if (data.cubes[i].stat == 2) {
                document.getElementById("r" + data.cubes[i].row + "c" + data.cubes[i].col).className = 'grid-item-yellow';
            } else {
                document.getElementById("r" + data.cubes[i].row + "c" + data.cubes[i].col).className = 'grid-item-red';
            }
        }
        /*if (data.cubes[0].stat == 0) {
            document.getElementById("r0c0").classList.remove('grid-item-yellow');
            document.getElementById("r0c0").classList.add('grid-item-red');
        }*/
    }
};
xmlhttp.open("GET", "data.txt", true);
xmlhttp.send();
