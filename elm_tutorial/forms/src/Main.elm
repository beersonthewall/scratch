module Main exposing (..)

import Browser
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput)

-- MAIN
main = Browser.sandbox { init = init, update = update, view = view }

-- MODEL
type alias Model = {
        name : String
        , password : String
        , passwordAgain : String
    }

init : Model
init = Model "" "" ""

-- UPDATE
type Msg = Name String
    | Password String
    | PasswordAgain String

update : Msg -> Model -> Model
update msg model =
    case msg of
        Name n -> { model | name = n }
        Password p -> { model | password = p }
        PasswordAgain pa -> { model | passwordAgain = pa }

-- VIEW
view : Model -> Html Msg
view model =
    div [] [ viewInput "text" "Name" model.name Name
              , viewInput "password" "Password" model.password Password
              , viewInput "password" "PasswordAgain" model.passwordAgain PasswordAgain
              , viewValidation model ]

viewInput : String -> String -> String -> (String -> msg) -> Html msg
viewInput t p v toMsg =
    input [ type_ t, placeholder p, value v, onInput toMsg ] []

viewValidation : Model -> Html msg
viewValidation model =
    if model.password == model.passwordAgain && String.length model.password > 8 then
        div [ style "color" "green" ] [ text "Ok" ]
    else
        div [ style "color" "red" ] [ text "Passwords don't match, or aren't long enough (8 chars)" ]

