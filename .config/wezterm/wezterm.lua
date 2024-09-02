local wezterm = require 'wezterm'
local config = wezterm.config_builder()

config.color_scheme = 'Monokai Remastered'
config.window_background_opacity = 0.8
config.font = wezterm.font 'Fira Code Nerdfont'
config.hide_tab_bar_if_only_one_tab = true
config.use_fancy_tab_bar = false
config.audible_bell = "Disabled"
config.visual_bell = {
  fade_in_duration_ms = 50,
  fade_out_duration_ms = 50,
}

config.skip_close_confirmation_for_processes_named = {'zsh'}

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

config.leader = { key = 'Space', mods = 'CTRL', timeout_milliseconds = 1000 }
config.keys = {
  {key = 'u', mods = 'ALT', action = wezterm.action.EmitEvent 'increase-opacity'},
  {key = 'd', mods = 'ALT', action = wezterm.action.EmitEvent 'decrease-opacity'},
  
  {key = "\\", mods = 'LEADER', action = wezterm.action.SplitHorizontal {domain = 'CurrentPaneDomain'},},
  {key = '-', mods = 'LEADER', action = wezterm.action.SplitVertical {domain = 'CurrentPaneDomain'},},
  
  {key = 'h', mods = 'ALT', action = wezterm.action.ActivatePaneDirection "Left"},
  {key = 'j', mods = 'ALT', action = wezterm.action.ActivatePaneDirection "Down"},
  {key = 'k', mods = 'ALT', action = wezterm.action.ActivatePaneDirection "Up"},
  {key = 'l', mods = 'ALT', action = wezterm.action.ActivatePaneDirection "Right"},
}

return config

