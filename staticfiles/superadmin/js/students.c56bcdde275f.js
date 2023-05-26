
// FAKULTET
const fakultetName = {
    "Fizika-matematika": [
        "Matematika va informatika", 
        "Matematika o'qitish metodikasi", 
        "Fizika va astronomiya", 
        "Fizika va astronomiya o'qitish metodikasi"
    ],
    "Pedagogika": [
        "Pedagogika va psixologiya", 
        "Psixologiya(amaliy psixologiya)", 
        "Maxsus pedagogika(logopediya)", 
        "Defektologiya(surdopedagogika)", 
        "Defektologiya(oligofrenopedagogika)", 
        "Defektologiya(Logopediya)"
    ],
    "Tarix": [
        "Tarix",
        "Tarix o'qitish metodikasi",
        "Milliy g'oya ma'naviyat asoslari va huquq ta'limi"
    ],
    "Milliy hunarmandchilik va amaliy san'at" : [
        "Musiqa ta'limi",
        "Tasviriy san'at va muhandislik grafikasi",
        "Texnologik ta'lim"
    ],
    "Rus tili va adabiyoti": [
        "Ona tili va adabiyoti(rus tili va adabiyoti)",
        "O'zga tilli guruhlarda rus tili",
        "Ona tili va adabiyoti(rus tili va adabiyoti(o'zga tilli guruhlarda))",
    ],
    "Tabiiy fanlar": [
        "Kimyo",
        "Kimyo o'qitish metodikasi",
        "Biologiya",
        "Biologiya o'qitish metodikasi",
        "Geografiya va iqtisodiy bilim asoslari",
        "Geografiya o'qitish metodikasi"
    ],
    "Xorijiy tillar": [
        "Xorijiy til va adabiyoti(ingliz tili)",
        "Maktabgacha va boshlang'ich ta'limda xorijiy til(ingliz tili)"
    ],
    "O'zbek tili va adabiyoti": [
        "O'zbek tili va adabiyoti"
    ],
    "Maktabgacha ta'lim": [
        "Maktabgacha ta'lim",
        "Maktabgacha ta'lim psixologiyasi va pedagogikasi",
        "Maktab menejmenti"
    ],
    "Boshlang'ich ta'lim": [
        "Boshlang'ich ta'lim",
        "Boshlang'ich ta'lim va sport tarbiyaviy ish"
    ],
    "Jismoniy madaniyat": [
        "Jismoniy madaniyat"
    ]
}


window.onload = function () {

    // FAKULTET
    const fakultetSelection = document.querySelector("#fakultet"),
    majorSelection = document.querySelector("#major");
    
    // todo: Disable all  Selection by setting disabled to false
    majorSelection.disabled = true;
    
    for (let fakultet in fakultetName) {
        fakultetSelection.options[fakultetSelection.options.length] = new Option(
            fakultet,
            fakultet
            );
        }
        // Region Changed
        fakultetSelection.onchange = (e) => {
            majorSelection.disabled = false;
            
            majorSelection.length = 1;
            
            // Load states by looping over fakultet
            for (let major of fakultetName[e.target.value]) {
                majorSelection.options[majorSelection.options.length] = new Option(
                    major,
                    major
                    );
                }
            };
        };