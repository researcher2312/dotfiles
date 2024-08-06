local wezterm = require 'wezterm'

local config = wezterm.config_builder()

config.color_scheme = 'Monokai Remastered'
config.window_background_opacity = 0.8
config.font = wezterm.font 'Fira Code Nerdfont'

config.skip_close_confirmation_for_processes_named = {'zellij', 'zsh'}

wezterm.on('increase-opacity', function(window, pane)
  local overrides = {}
  overrides.window_background_opacity = window:effective_config().window_background_opacity - 0.1
  window:set_config_overrides(overrides)
end)

wezterm.on('decrease-opacity', function(window, pane)
  local overrides = {}
  overrides.window_background_opacity = window:effective_config().window_background_opacity + 0.1
  window:set_config_overrides(overrides)
end)

config.keys = {
  -- CTRL+SHIFT+Space, followed by 'r' will put us in resize-pane
  -- mode until we cancel that mode.
  {
    key = 'u',
    mods = 'ALT',
    action = wezterm.action.EmitEvent 'increase-opacity',
  },
  {
    key = 'd',
    mods = 'ALT',
    action = wezterm.action.EmitEvent 'decrease-opacity',
  },
}

return config

