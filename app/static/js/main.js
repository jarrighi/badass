$(document).ready(function(){
  console.log('ready')
  // TODO: use underscore or lodash for this
  var html_block = '<form method="post" action="/add_skill">' +
  '<label for="skill_name">skill</label>' +
  '<input type="text" name="skill_name" id="skill_name">' +
  '<label for="skill_description">describe your skill</label>' +
  '<input type="text" name="skill_description" id="skill_description">' +
  '<label for="skill_level">Assign a level to this skill (1, 3, or 5)</label>' +
  '<input type="text" name="skill_level" id="skill_level">' +
  '<input type="submit" name="submit" id="submit">' +
  '</form>';

  $("button").on("click", function bindButtonClick(){
    $('#add-skill').html(html_block); // end html
    $('form').on("submit", function(evt) {
      evt.preventDefault();
      var url = $(this).attr("action");
      var formData = $(this).serialize();
      $.post(url, formData, function(response){
        $('#add-skill').html("<button>Add a skill</button>")
        $("button").on("click", bindButtonClick);
      }); // end post
    }); // end submit
  }); //end click
}); // end ready

// TODO: hide and show instead of replacing html in #add-skill