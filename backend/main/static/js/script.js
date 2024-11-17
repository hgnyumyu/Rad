$(function () {
 $(".sidebar-link").click(function () {
  $(".sidebar-link").removeClass("is-active");
  $(this).addClass("is-active");
 });
});

$(window)
 .resize(function () {
  if ($(window).width() > 1090) {
   $(".sidebar").removeClass("collapse");
  } else {
   $(".sidebar").addClass("collapse");
  }
 })
 .resize();


$(function () {
 $(".logo, .logo-expand, .discover").on("click", function (e) {
  $(".main-container").removeClass("show");
  $(".main-container").removeClass("show_setting");
  $(".main-container").removeClass("show_test");
  $(".main-container").removeClass("show_group");
  $(".main-container").removeClass("show_learn");
  $(".main-container").scrollTop(0);
 });
 $(".trending").on("click", function (e) {
  $(".main-container").addClass("show");
  $(".main-container").removeClass("show_setting");
  $(".main-container").removeClass("show_learn");
  $(".main-container").removeClass("show_test");
  $(".main-container").removeClass("show_group");
  $(".main-container").scrollTop(0);
  $(".sidebar-link").removeClass("is-active");
  $(".trending").addClass("is-active");
 });
 $(".setting").on("click", function (e) {
    $(".main-container").addClass("show_setting");
    $(".main-container").removeClass("show");
    $(".main-container").removeClass("show_test");
    $(".main-container").removeClass("show_learn")
    $(".main-container").removeClass("show_group");;
    $(".main-container").scrollTop(0);
    $(".sidebar-link").removeClass("is-active");
    $(".setting").addClass("is-active");
   });
   $(".video").on("click", function (e) {
    $(".main-container").addClass("show_test");
    $(".main-container").removeClass("show");
    $(".main-container").removeClass("show_setting");
    $(".main-container").removeClass("show_learn");
    $(".main-container").removeClass("show_group");
    $(".sidebar-link").removeClass("is-active");
    $(".main-container").scrollTop(0);
    $(".discover").addClass("is-active");
   });
   $(".learning").on("click", function (e) {
    $(".main-container").addClass("show_learn");
    $(".main-container").removeClass("show");
    $(".main-container").removeClass("show_setting");
    $(".main-container").removeClass("show_test");
    $(".main-container").removeClass("show_group");
    $(".sidebar-link").removeClass("is-active");
    $(".main-container").scrollTop(0);
    $(".learning").addClass("is-active");
   });
   
});
function init(e) {
    if (!e.target.closest('.item')) return;
    let hero = document.querySelector('div[data-pos="0"]');
    let target = e.target.parentElement;
    [target.dataset.pos,hero.dataset.pos] = [hero.dataset.pos,target.dataset.pos];
  }
  
  window.addEventListener('click',init,false);

/**
 * карта знаний radar
 */
let ctx = 
            document.getElementById('radarChart').getContext('2d');
        let myRadarChart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels:
                    ['fullstack', 'DS', 'GD',
                    'CS'],
                datasets: [{
                    label: 'Yours Skills',
                    data: [100, 85, 10, 10],
                    backgroundColor: 'rgba(245, 166, 39, 0.64)',
                    borderColor: 'rgba(75, 192, 0, 1)',
                    borderWidth: 2,
                }]
            },
			
            options:  {
				scales: {
					r: {
						 angleLines: {
							color: 'red'
						},
						grid: {
							color: 'red'
						},
						backgroundColor: 'rgba(39, 213, 245, 0.33)'
					}
				}
			}
        });
/*graphChart*/
let data = {
    "nodes": [
     {
        "id": "USER",
        "fill":{
          "color":"rgba(245, 40, 145, 0.8)"
        }
      },
      {
        "id": "FullStack",
        "fill":{
          "color":"rgba(208, 245, 39, 0.8)"
        }
      },
      {
        "id": "Frontend",
         "fill":{
          "color":"rgba(245, 0, 0, 1)"
        }
      },
      {
        "id": "HTML",
        "fill":{
          "color":"rgba(39, 245, 63, 0.8)"
        }
      },
      {
        "id": "CSS",
         "fill":{
          "color":"rgba(245, 0, 0, 1)"
        }
      },
      {
        "id": "JavaScript",
         "fill":{
          "color":"rgba(245, 0, 0, 1)"
        }
      },
      {
        "id": "Backend",
         "fill":{
          "color":"rgba(245, 0, 0, 1)"
        }
      },
      {
        "id": "C++",
        "fill":{
          "color":"rgba(39, 245, 63, 0.8)"
        }
      },
      {
        "id": "Python",
        "fill":{
          "color":"rgba(39, 245, 63, 0.8)"
        }
      },
      {
        "id": "DataSciense",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "СУБД",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "SQL",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "SkyPython",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "CyberSecurity",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "Linux",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "Network",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "GameDev",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "Unity",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "C#",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      },
      {
        "id": "UnrealEngine",
         "fill":{
          "color":"rgba(17, 0, 0, 0.4)"
        }
      }
    ],
    "edges": [
    {
        "from": "USER",
        "to": "GameDev"
      },
    {
        "from": "USER",
        "to": "FullStack"
      },
    {
        "from": "USER",
        "to": "DataSciense"
      },
    {
        "from": "USER",
        "to": "CyberSecurity"
      },
      {
        "from": "FullStack",
        "to": "Frontend"
      },
      {
        "from": "FullStack",
        "to": "Backend"
      },
      {
        "from": "Frontend",
        "to": "HTML"
      },,
      {
        "from": "Frontend",
        "to": "CSS"
      },
      ,
      {
        "from": "Frontend",
        "to": "JavaScript"
      },
      {
        "from": "Backend",
        "to": "C++"
      },
      ,
      {
        "from": "Backend",
        "to": "Python"
      },
      
      {
        "from": "DataSciense",
        "to": "СУБД"
      },
      {
        "from": "СУБД",
        "to": "SQL"
      },
      {
        "from": "DataSciense",
        "to": "SkyPython"
      },
      {
        "from": "SkyPython",
        "to": "Python"
      },
      {
        "from": "CyberSecurity",
        "to": "СУБД"
      },
      {
        "from": "CyberSecurity",
        "to": "Linux"
      },
      {
        "from": "Linux",
        "to": "Network"
      },
      {
        "from": "GameDev",
        "to": "Unity"
      },
      {
        "from": "Unity",
        "to": "C#"
      },
      {
        "from": "UnrealEngine",
        "to": "C++"
      },
      {
        "from": "GameDev",
        "to": "UnrealEngine"
      }
    ]
  }
        anychart.onDocumentReady(function () {
          //anychart.data.loadJsonFile("./lol.json", function (data) {
          // create a chart from the loaded data
          var chart = anychart.graph(data);
          // set the title
          
          var title = chart.title();
          title.enabled(true);
          title.text('Дорожная карта развития навыков');
          
          // Get background.
          var background = title.background();
          background.enabled(true);
          background.fill('#43F4DD 0.2');
          background.stroke('#2196F3 0.4');
          background.corners(10);
          // draw the chart
          
          var nodes = chart.nodes();
          chart.nodes().labels().enabled(true);
          chart.nodes().labels().format("{%id}");
          chart.nodes().labels().fontSize(12);
          chart.nodes().labels().fontWeight(600);
          chart.container("graphChart").draw();
          //});
        });
