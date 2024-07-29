$(document).ready(function() {
    $('.like-btn').click(function() {
        var post_id = $(this).data('post-id');
        var button = $(this);
        var like_count = $('#like-count-' + post_id);

        $.ajax({
            url: '{% url "like_post" post_id=0 %}'.replace('0', post_id),
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(data) {
                if (data.liked) {
                    button.find('i').removeClass('fa-regular').addClass('fa-solid');
                } else {
                    button.find('i').removeClass('fa-solid').addClass('fa-regular');
                }
                like_count.text(data.like_count);
            }
        });
    });
});