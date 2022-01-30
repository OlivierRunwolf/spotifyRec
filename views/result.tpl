<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Title</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
          integrity="sha512-Fo3rlrZj/k7ujTnHg4CGR2D7kSs0v4LLanw2qksYuRlEzO+tcaEPQogQ0KaoGN26/zrn20ImR1DfuLWnOo7aBA=="
          crossorigin="anonymous" referrerpolicy="no-referrer"/>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"
            integrity="sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ=="
            crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/howler/2.2.3/howler.min.js"
            integrity="sha512-6+YN/9o9BWrk6wSfGxQGpt3EUK6XeHi6yeHV+TYD2GR0Sj/cggRpXr1BrAQf0as6XslxomMUxXp2vIl+fv0QRA=="
            crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <link href="/css/tinyPlayer.css" rel="stylesheet"/>
    <script src="/js/tinyPlayer.js"></script>
    <style>
        img {
            border-radius: 50%;
        }
        a{
            color: wheat !important;
        }
    </style>
</head>
<body>
<table class="table table-hover table-dark">
    <thead>
    <tr>
        <th scope="col">image</th>
        <th scope="col">artist</th>
        <th scope="col">song name</th>
        <th scope="col">album</th>
        <th scope="col">preview</th>
    </tr>
    </thead>
    <tbody>
    % for item in tracks:
    <tr><!--{{item['album']['images'][0]['url']}}-->
        <th scope="row"><img src="{{item['album']['images'][0]['url']}}" alt="Girl in a jacket" width="40" height="40">
        </th>
        <td>
            % for art in item['artists']:
            <a href="{{art['external_urls']['spotify']}}" target="_blank"
               style="text-decoration: none;">{{art['name']}}</a> ,
            % end
        </td>
        <td><a href="{{item['external_urls']['spotify']}}" target="_blank" style="text-decoration: none;">{{item['name']}}</a>
        </td>
        <td><a href="{{item['album']['external_urls']['spotify']}}" target="_blank" style="text-decoration: none;">{{item['album']['name']}}</a>
        </td>
        <td>
            <audio controls class="iru-tiny-player" data-title="{{item['name']}}">
                <source src="{{item['preview_url']}}}" type="audio/mpeg">
            </audio>
        </td>
    </tr>
    % end
    </tbody>
</table>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
</body>
</html>