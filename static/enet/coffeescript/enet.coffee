$ ->
  $(".date").datepicker(
    changeYear: true
    yearRange: "-35:-18"
  )
  $(".datetime").datetimepicker()
  $("a[href^=#]").click( (e) ->)
  $("#feedbackbutton").click( ->
    $("#feedbackarea").load("/pages/feedback/")
  )
  $("#registerbutton").click( ->
    $.pgwModal(
      url: '/register/',
      loadingContent: '<span style="text-align:center">Loading in progress</span>',
      titleBar: false
    )
    return false;
  )
  $('.pgwSlider').pgwSlider(
    intervalDuration: 8000,
    displayControls: true
  )
PersonDialog = (wrapper) ->
  self = this
  @wrapper = wrapper
  @filter = @wrapper.find(".filter")
  @labels = @wrapper.find(".thumbnail p")
  @imgs = @wrapper.find("img").parent().parent()
  @labels.hide()
  @chosen = ->
    @imgs.find ".selected img"


  #Create the dialog window
  @wrapper.dialog
    appendTo: self.wrapper.parent()
    create: self.timer = refresh = setInterval(->
      console.log "running"
      self.imgs.hide()
      self.imgs.filter(":contains('" + self.filter.val() + "')").show()
      return
    , 500)
    close: ->
      clearInterval self.timer
      return

  @wrapper.dialog "option", "width", 550

  #Initiate the autocomplete plugin
  acsrc = @labels.contents()
  @ac = []
  acsrc.each (item) ->
    self.ac.push acsrc[item].data
    return

  @filter.autocomplete source: self.ac

  # Prevent Enter Keypresses from submitting the form
  @filter.keypress (event) ->
    event.preventDefault()  if event.keyCode is 13
    return

  return

