
var dot_probe_procedure = {
    timeline: [
        {
            type: 'html-keyboard-response',
            stimulus: "+",
            choices: jsPsych.NO_KEYS,
            trial_duration: 500
        },
        {
            type: 'html-keyboard-response',
            stimulus: jsPsych.timelineVariables('stimuli'),
            choices: jsPsych.NO_KEYS,
            trial_duration: 100
        },
        {
            type: 'html-keyboard-response',
            stimulus: jsPsych.timelineVariables('probe'),
            choices: jsPsych.timelineVariables('probe')
        },
        on_finish: function(data)
    ],
    timeline_variables: [
        {stimuli: "chair"},
        {stimuli: "washer"},
        {probe: "c"},
        {probe: "a"}


    ]
}