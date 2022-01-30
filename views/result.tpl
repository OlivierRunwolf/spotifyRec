<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Title</title>
</head>
<body>
<table class="table table-dark">
    <thead>
    <tr>
        <th scope="col">image</th>
        <th scope="col">artist</th>
        <th scope="col">song name</th>
        <th scope="col">album</th>
    </tr>
    </thead>
    <tbody>
    % for item in tracks:
        <tr><!--{{item['album']['images'][0]['url']}}-->
          <th scope="row"><img src="{{item['album']['images'][0]['url']}}" alt="Girl in a jacket" width="40" height="40"></th>
          <td>
              % for art in item['artists']:
              {{art['name']}}
              % end
          </td>
          <td>{{item['name']}}</td>
          <td>{{item['album']['name']}}</td>
        </tr>
    % end
    </tbody>
</table>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
</body>
</html>