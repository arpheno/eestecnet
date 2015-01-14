$ ->
  $(".date").datepicker(
    changeYear: true
    yearRange: "-35:-18"
  )
  $(".datetime").datetimepicker()
  $("a[href^=#]").click( (e) ->)
  $("#feedbackbutton").click( ->
    $.pgwModal(
      url: '/pages/feedback/',
      loadingContent: '<span style="text-align:center">Loading in progress</span>',
      titleBar: false
    )
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
root = exports ? this
root.PersonDialog = (wrapper) ->
  self = this
  @wrapper = wrapper
  @filter = @wrapper.find(".filter")
  @labels = @wrapper.find(".thumbnail p")
  @wrapper.find("select").imagepicker(
    show_label: true
  )
  @imgs = @wrapper.find("img").parent().parent()
  @chosen = ->
    @imgs.find ".selected img"
  self.filter.keyup((e) ->
      self.imgs.hide()
      self.imgs.filter(":contains('" + self.filter.val() + "')").show()
  )
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

