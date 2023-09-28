// takes note id that we passed and send a post request to the delete node endpoint
// and after it gets a response from the delete node endpoint it is going to reload the window
function deleteNote(noteId) {
    fetch("/delete-note", {
        method: 'POST',
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}
function deleteImage(image_id) {
    fetch("/delete-image", {
        method: 'POST',
        body: JSON.stringify({imageId: image_id}),
    }).then((_res) => {
        window.location.href = "/";
    });
}