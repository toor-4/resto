<script>
  function expandParagraph() {
    var paragraph = document.querySelector("article p");
    paragraph.classList.remove("collapsed");
    paragraph.style.maxHeight = paragraph.scrollHeight + "px";
    var button = document.querySelector("article button");
    button.style.display = "none";
  }
</script>