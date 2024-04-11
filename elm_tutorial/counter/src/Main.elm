module Main exposing (..)

import Browser
import Html exposing (Html, button, div, text)
import Html.Events exposing (onClick)

-- MAIN

main =
    Browser.sandbox { init = init, update = update, view = view }

-- MODEL

type alias Model = Int

init : Model
init =
    0

-- UPDATE

type Msg = Increment Int | Decrement Int | Reset

update : Msg -> Model -> Model
update msg model =
    case msg of
        Increment i -> model + i
        Decrement i -> model - i
        Reset -> 0

-- VIEW
view : Model -> Html Msg
view model =
    div []
        [ button [ onClick (Decrement 1) ] [ text "-" ]
              , button [ onClick (Decrement 5) ] [ text "- 5" ]
              , div [] [ text (String.fromInt model) ]
              , button [ onClick (Increment 1) ] [ text "+" ]
              , button [ onClick (Increment 5) ] [ text "+ 5" ]
              , div [] []
              , button [ onClick Reset ] [ text "reset" ]
        ]
