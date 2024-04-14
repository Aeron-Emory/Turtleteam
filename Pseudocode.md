# Code Explained or something?

> ## Main()
> 
> ### Declare the `screen`
> 
> ### Ask for `Background Color`
> ### Call function 1 and send `Background Color` to it
>
> ### Ask for `Pattern Shape`
> ### Call function 2 and send `Pattern Shape` to it
>
> ### Ask for what `Shape`
> ### Call function 3 and send `Shape` to it
>
> ### Ask for `Letter`
> ### Call function 4 and send `Letter` to it

***
> ## Function 1 (Set Background Color)
>
> ### Use `Background Color` from main() to change color of background

***
> ## Function 2 (Grid Pattern)
>
> ### Get Screen `height` and `width`
>
> ### if `Pattern Shape` == `Grid`
> > #### Call Function Vertical and send `height` and `width`
> > #### Call Function Horizontal and send `height` and `width`
> 
> ### elif `Pattern Shape` == `Stripes`
> > #### Ask for `stripe direction`
> > 
> > #### if `stripe direction` == `horizontal`
> > > ##### Call Function Horizontal and send `height` and `width`
> > > 
> > #### elif `stripe direction` == `Vertical`
> > > ##### Call Function Vertical and send `height` and `width`
> > > 
> > #### else:
> > > ##### print = Invalid stripe direction. Please enter 'horizontal' or 'vertical'
> 
> ### elif `pattern` == `Diagonal` __(not implemented properly)__
> > #### Ask if `/` or `\`
> > #### if `/`
> > > ##### Call Function Diagonal and send `height` and `width`
> > 
> > #### elif `\`
> > > ##### Call Function DiagonalR and send `height` and `width`
> >
> > #### else
> > > ##### print = invalid response
>
> ### elif `pattern` == `Diagrid`
> > #### Call Function DiagonalR and send `height` and `width`
> > #### Call Function DiagonalR and send `height` and `width`
> >
> ### else|
> > #### print = invalid response

***
> ## Function 2.1 (Horizontal line)
> ### Ask for what `spaceing between each line` __(not implemented properly)__m,
> ### Calculating Number of lines
> ### number of lines to draw = height // `spaceing between each line`
> ### For loop with range (from: `-num_cells_y // 2` to `num_cells_y // 2 + 1`)
> ```
> explanation of math
> Since we can't just use the spaceing between each line variable raw we have to adjust and center it.
> For example lets say we need 6 lines (calculated if height is 300)
> so, we can't just use the 6 in the for loop since turle does that (0,0) coord thing
> Therefore, we need to do it such that -3 to 3 to evenly distribute
> -num_cells_y // 2 (half it and negative)
> num_cells_y // 2 + 1 (+1 cause python would just stop at 2)
> ```
> > #### on doing slight provocations