import Html.App as App
import Html exposing (..)
import Html.Attributes exposing (href, class, style)

import Material
import Material.Scheme
import Material.Button as Button
import Material.Options exposing (css)
import Material.Layout as Layout
import Material.Color as Color

-- Model
type alias Model = 
    { count : Int
    , mdl : Material.Model
        -- Boilerplate: model store for any and all Mdl components
    , selectedTab : Int
    }

model : Model
model = 
    { count = 0
    , mdl = Material.model
    -- Boilerplate: Always use this initial Mdl model store.
    , selectedTab = 0
    }

-- Action, Update

type Msg = 
    Increase
    | Reset
    | Mdl (Material.Msg Msg)
    | SelectTab Int

update : Msg -> Model -> (Model, Cmd Msg)
update msg model = 
    case msg of
        Increase ->
            ( { model | count = model.count + 1}
            , Cmd.none)

        Reset ->
            ( { model | count = 0 }
            , Cmd.none)

        SelectTab num ->
            { model | selectedTab = num } ! []

        -- Boilerplate: mdl action handler.
        Mdl msg' ->
            Material.update msg' model

-- View

type alias Mdl =
    Material.Model

view : Model -> Html Msg
view model =
    Material.Scheme.topWithScheme Color.Amber Color.Yellow <|
        Layout.render Mdl
            model.mdl
            [ Layout.fixedHeader
            , Layout.onSelectTab SelectTab
            ]
            { header = [ h1 [ style [ ( "padding", "2rem" ) ] ] [ text "Counter" ] ]
            , drawer = []
            , tabs = ( [ text "Milk" , text "Oranges" ], [] )
            , main = [ viewBody model ]
            }

viewBody : Model -> Html Msg
viewBody model =
    case model.selectedTab of
        0 ->
            viewCounter model
        1 ->
            text "something else"
        _ -> 
            text "404"

viewCounter : Model -> Html Msg
viewCounter model = 
    div 
        [ style [ ("padding", "2rem") ] ]
        [ text ("Current count: " ++ toString model.count)
        {- We construct the instane of the Button component that we need, one
        for the increase button and one for the reset button. 
        1. The increase button. The first three arguments are:
            - A Msg constructor (`Mdl`), lifting Mdl message to the Msg type
            - An instance id (the `[0]`). Evernt component that uses the same model collection (model.mdl in this file) must have a distinct instance id.
            - A reference to the elm-mdl model collection (`model.mdl`)

        Notice that we do not have to add fields for the increase and reset buttons
        separately to our model; and we did not have to add to our update messages
        to handle their internal events.

        Mdl components are configured with `Options`, similar to `Html.Attributes`.
        The `Button.onClick Increase` option instructs the button to sent the `Increase` message when clicked. The `css ...` option adds CSS styling to the button.
        See `Material.Options` for details on options.
        -}
        , Button.render Mdl [0] model.mdl
            [ Button.onClick Increase
            , css "margin" "0 24px"
            ]
            [ text "Increase" ]
        , Button.render Mdl [1] model.mdl
            [ Button.onClick Reset ]
            [ text "Reset" ]
        ]
        
main : Program Never
main =
    App.program
        { init = ( model, Cmd.none )
        , view = view
        , subscriptions = always Sub.none
        , update = update
        }

